package com.example.loadbalancer;

import java.io.Serializable;

/**
 * Created by Samodha Pallewatta on 4/8/2021.
 */
public class Product implements Serializable {
    private String product_serial_num;
    private String product_name;
    private Double price;
    private Integer available_quantity;

    public Double getPrice() {
        return price;
    }

    public Integer getAvailable_quantity() {
        return available_quantity;
    }

    public String getProduct_name() {
        return product_name;
    }

    public String getProduct_serial_num() {
        return product_serial_num;
    }

    public void setAvailable_quantity(Integer available_quantity) {
        this.available_quantity = available_quantity;
    }

    public void setPrice(Double price) {
        this.price = price;
    }

    public void setProduct_name(String product_name) {
        this.product_name = product_name;
    }

    public void setProduct_serial_num(String product_serial_num) {
        this.product_serial_num = product_serial_num;
    }
}
