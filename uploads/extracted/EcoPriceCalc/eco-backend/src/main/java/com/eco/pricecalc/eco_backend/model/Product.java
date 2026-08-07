package com.eco.pricecalc.eco_backend.model;

import jakarta.persistence.*;

@Entity
@Table(name = "products")
public class Product {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;  // MySQL 'int' -> Java Integer

    private String name;

    @Column(columnDefinition = "text")
    private String description;

    @Column(precision = 10, scale = 2)
    private Double price;

    @Column(name = "sustainability_score")
    private Integer sustainabilityScore;

    @Column(name = "eco_price", precision = 10, scale = 2)
    private Double ecoPrice;

    // Getters and Setters
    public Integer getId() { return id; }
    public void setId(Integer id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }

    public Double getPrice() { return price; }
    public void setPrice(Double price) { this.price = price; }

    public Integer getSustainabilityScore() { return sustainabilityScore; }
    public void setSustainabilityScore(Integer sustainabilityScore) { this.sustainabilityScore = sustainabilityScore; }

    public Double getEcoPrice() { return ecoPrice; }
    public void setEcoPrice(Double ecoPrice) { this.ecoPrice = ecoPrice; }
}
