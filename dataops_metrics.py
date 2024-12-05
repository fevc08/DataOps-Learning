import time
import logging
import random

# Configure logging
logging.basicConfig(
    filename='pipeline_metrics.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def mock_pipeline(data):
    start_time = time.time()
    processed_records = 0
    error_count = 0

    logging.info("Pipeline started.")

    for record in data:
        try:
            # Simulate processing with a small delay
            time.sleep(0.1)
            if random.random() < 0.1:  # Simulate a 10% error rate
                raise ValueError("Processing error")
            processed_records += 1
        except Exception as e:
            error_count += 1
            logging.error(f"Error processing record {record}: {e}")

    duration = time.time() - start_time
    logging.info(f"Pipeline completed in {duration:.2f} seconds.")
    logging.info(f"Processed records: {processed_records}")
    logging.info(f"Error count: {error_count}")
    logging.info(f"Success rate: {processed_records / len(data) * 100:.2f}%")

    return {
        "duration": duration,
        "processed_records": processed_records,
        "error_count": error_count,
        "success_rate": processed_records / len(data) * 100
    }

if __name__ == "__main__":
    # Mock data
    data = list(range(1, 101))  # 100 mock records
    metrics = mock_pipeline(data)

    print("\nPipeline Metrics:")
    for key, value in metrics.items():
        print(f"{key.capitalize()}: {value}")
