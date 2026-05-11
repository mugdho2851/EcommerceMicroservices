package com.ecommerce.order.service;

import com.ecommerce.order.entity.Order;
import com.ecommerce.order.repository.OrderRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.List;
import java.util.Map;
import java.util.Optional;

@Service
public class OrderService {
    
    @Autowired
    private OrderRepository orderRepository;
    
    private final RestTemplate restTemplate = new RestTemplate();
    private final String USER_SERVICE_URL = "http://localhost:8081/users";
    private final String PRODUCT_SERVICE_URL = "http://localhost:8082/products";
    
    public Order createOrder(Order order) {
        try {
            restTemplate.getForObject(USER_SERVICE_URL + "/" + order.getUserId(), Map.class);
        } catch (Exception e) {
            throw new RuntimeException("User not found with ID: " + order.getUserId());
        }
        
        try {
            Map<String, Object> product = restTemplate.getForObject(
                PRODUCT_SERVICE_URL + "/" + order.getProductId(), Map.class);
            double price = (double) product.get("price");
            order.setTotalPrice(price * order.getQuantity());
        } catch (Exception e) {
            throw new RuntimeException("Product not found with ID: " + order.getProductId());
        }
        
        return orderRepository.save(order);
    }
    
    public List<Order> getAllOrders() {
        return orderRepository.findAll();
    }
    
    public Optional<Order> getOrderById(Long id) {
        return orderRepository.findById(id);
    }
}

