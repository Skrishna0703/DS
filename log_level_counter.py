import os
from collections import defaultdict
from multiprocessing import Pool

# Mapper function
def mapper(chunk):
    counts = defaultdict(int)
    for line in chunk:
        log_level = line.split()[0]  # Assume log level is the first word
        counts[log_level] += 1
    return counts

# Reducer function
def reducer(mapped_results):
    final_counts = defaultdict(int)
    for result in mapped_results:
        for log_level, count in result.items():
            final_counts[log_level] += count
    return final_counts

# Function to divide the file into chunks for parallel processing
def chunk_file(file_path, num_chunks):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Divide the lines into chunks
    chunk_size = len(lines) // num_chunks
    chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]
    
    return chunks

# Main function
def log_level_count(file_path, num_chunks=4):
    # Step 1: Divide the file into chunks
    chunks = chunk_file(file_path, num_chunks)
    
    # Step 2: Use multiprocessing to map the chunks
    with Pool(processes=num_chunks) as pool:
        mapped_results = pool.map(mapper, chunks)
    
    # Step 3: Reduce the results to get the final counts
    final_counts = reducer(mapped_results)
    
    # Output the results
    for log_level, count in final_counts.items():
        print(f'{log_level}: {count}')

if __name__ == '__main__':
    log_level_count('logs.txt', num_chunks=4)  # Adjust the file path and number of chunks as needed
