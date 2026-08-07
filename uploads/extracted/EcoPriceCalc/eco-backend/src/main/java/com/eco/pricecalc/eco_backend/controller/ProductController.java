package com.eco.pricecalc.eco_backend.controller;

import com.eco.pricecalc.eco_backend.model.Product;
import com.eco.pricecalc.eco_backend.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/products")
@CrossOrigin(origins = "http://localhost:3000") // Enables React frontend to access API
public class ProductController {

    @Autowired
    private ProductRepository productRepository;

    @GetMapping
    public List<Product> getProducts() {
        return productRepository.findAll();
    }

    @PostMapping
    public Product addProduct(@RequestBody Product product) {
        // Example: Calculate ecoPrice based on your logic
        double ecoPrice = product.getPrice();
        if (product.getSustainabilityScore() != null && product.getPrice() != null) {
            ecoPrice = product.getPrice() * (1 - product.getSustainabilityScore() / 100.0);
        }
        product.setEcoPrice(ecoPrice);
        return productRepository.save(product);
    }
}
