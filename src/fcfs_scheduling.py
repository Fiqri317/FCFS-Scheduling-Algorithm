class Request:
    def __init__(self, name, arrival_time, processing_time):
        self.name = name
        self.arrival_time = arrival_time
        self.processing_time = processing_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def calculate_fcfs(requests):
    current_time = 0

    for request in requests:
        # Update waktu saat ini jika lebih kecil dari waktu kedatangan permintaan
        if current_time < request.arrival_time:
            current_time = request.arrival_time

        # Hitung waktu penyelesaian
        current_time += request.processing_time
        request.completion_time = current_time

        # Hitung waktu turnaround
        request.turnaround_time = request.completion_time - request.arrival_time

        # Hitung waktu tunggu
        request.waiting_time = request.turnaround_time - request.processing_time

def display_results(requests):
    print(f"{'Permintaan':<15}{'Kedatangan':<15}{'Proses':<10}{'Penyelesaian':<15}{'Turnaround':<15}{'Tunggu':<10}")
    for request in requests:
        print(f"{request.name:<15}{request.arrival_time:<15}{request.processing_time:<10}{request.completion_time:<15}{request.turnaround_time:<15}{request.waiting_time:<10}")

if __name__ == "__main__":
    # Data permintaan untuk sistem manajemen antrian pada server web
    web_requests = [
        Request("A", 0, 5),
        Request("B", 1, 3),
        Request("C", 2, 8),
        Request("D", 3, 6),
        Request("E", 4, 4)
    ]

    # Hitung FCFS
    calculate_fcfs(web_requests)

    # Tampilkan hasil
    display_results(web_requests)
