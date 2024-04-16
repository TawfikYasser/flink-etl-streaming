package FlinkETLStreaming.Dto;

import lombok.Data;

import java.sql.Timestamp;
@Data
public class Transaction {
    private String transactionId, productId, productName, productCategory, productBrand, currency, customerId, paymentMethod;
    private double productPrice, totalAmount;
    private int productQuantity;
    private Timestamp transactionDate;

}
