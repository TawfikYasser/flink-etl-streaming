package FlinkETLStreaming.Dto;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class SalesPerMonth {
    private int month, year;
    private double totalSales;
}
