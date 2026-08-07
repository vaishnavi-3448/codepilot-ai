package com.eco.pricecalc.eco_backend.repository;

import com.eco.pricecalc.eco_backend.model.Product;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ProductRepository extends JpaRepository<Product, Integer> {
    // Standard CRUD methods are provided by JpaRepository
}
