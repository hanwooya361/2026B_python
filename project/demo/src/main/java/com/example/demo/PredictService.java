package com.example.demo;

import java.io.IOException;
import java.util.Map;
import java.util.concurrent.CopyOnWriteArrayList;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;
import org.springframework.web.servlet.mvc.method.annotation.SseEmitter;

import lombok.RequiredArgsConstructor;

@Service 
@RequiredArgsConstructor 
public class PredictService {
    private final CopyOnWriteArrayList<SseEmitter> emitters = new CopyOnWriteArrayList<>();

    @Value("${fastapi.url}")
    private String fastApiUrl;
    // 다른 서버 호출 라이브러리
    WebClient webClient = WebClient.builder().build();
    // sse 구독: react가 접속하면 통로 만들어 리스트에 저장
    public SseEmitter subscribe(){
        SseEmitter emitter = new SseEmitter();  // 통로 생성
        emitters.add(emitter);                  // 리스트 저장
        emitter.onCompletion(() -> emitters.remove(emitter));
        try {   
            emitter.send(SseEmitter.event().name("connect").data("연결 완료"));
        } catch (IOException e) {
            emitters.remove(emitter);
        }
        return emitter;
    }

    // 메세지 전송: 구독중인 모든 클라이언트에게 이벤트 이름,데이터 전송
    public void onMessage(String name, Object data){
        for(SseEmitter emitter : emitters){
            try{
                emitter.send(SseEmitter.event().name(name).data(data));
            }catch(IOException e){
                emitters.remove(emitter);
            }
        }
    }

    // 추론 요청: fastapi에 예측 요청
    public void predict(PredictDto dto){
        webClient.post()
            .uri(fastApiUrl+"/api/predict")
            .contentType(MediaType.APPLICATION_JSON)
            .bodyValue(dto)
            .retrieve()
            .bodyToFlux(Map.class)
            .subscribe(
                result -> onMessage("result", result),
                error -> onMessage("fail", "AI 서버 오류")
            );
    }
}   
