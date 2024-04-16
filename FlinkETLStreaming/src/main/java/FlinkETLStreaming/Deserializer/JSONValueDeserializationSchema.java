package FlinkETLStreaming.Deserializer;

import FlinkETLStreaming.Dto.Transaction;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.flink.api.common.serialization.DeserializationSchema;
import org.apache.flink.api.common.typeinfo.TypeInformation;
import org.apache.flink.util.Collector;

import java.io.IOException;

public class JSONValueDeserializationSchema implements DeserializationSchema<Transaction> {

    private final ObjectMapper objectMapper = new ObjectMapper();

    @Override
    public void open(InitializationContext context) throws Exception {
        DeserializationSchema.super.open(context);
    }

    @Override
    public Transaction deserialize(byte[] bytes) throws IOException {
        return objectMapper.readValue(bytes, Transaction.class);
    }

//    @Override
//    public void deserialize(byte[] message, Collector<Transaction> out) throws IOException {
//        DeserializationSchema.super.deserialize(message, out);
//    }

    @Override
    public boolean isEndOfStream(Transaction transaction) {
        return false;
    }

    @Override
    public TypeInformation<Transaction> getProducedType() {
        return TypeInformation.of(Transaction.class);
    }
}
