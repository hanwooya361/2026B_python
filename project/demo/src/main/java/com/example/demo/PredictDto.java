package com.example.demo;

import com.fasterxml.jackson.annotation.JsonProperty;

public record PredictDto (
    String make,
    @JsonProperty("vehicle_class") String vehicleClass,
    @JsonProperty("engine_size") Double engineSize,
    Integer cylinders,
    String transmission,
    @JsonProperty("fuel_type") String fuelType    
){
    
}