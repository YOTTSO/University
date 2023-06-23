class HeapSort
{
public:
	void swap(int* a, int* b);
	void swap(char* a, char* b);
	void heapify(int arr[], int N, int i);
	void heapSort(int arr[], int N);
	void heapify(char arr[], int N, int i);
	void heapSort(char arr[], int N);
	void printArray(int arr[], int N);
	void printArray(char arr[], int N);
	void inputCheck(int arr[], char charr[],int size);
};

