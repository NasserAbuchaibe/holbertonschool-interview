#include "sort.h"

/**
 * maxHeapify - makes array into a heap
 * @array: pointer to int array
 * @size: size  array
 * @i: max point
 * @orig_size: initial array size
 * Return: void
 */
void maxHeapify(int *array, int size, int i, int orig_size)
{
	int max = i;
	int left = 2 * i + 1;
	int right = 2 * i + 2;

	if (left < size && array[max] < array[left])
	{
		max = left;
	}

	if (right < size && array[max] < array[right])
	{
		max = right;
	}

	if (max != i)
	{
		swap(&array[i], &array[max]);
		print_array(array, orig_size);
		maxHeapify(array, size, max, orig_size);
	}
}

/**
 * heap_sort - heap sort
 * @array: pointer to array
 * @size: size of array
 * Return: void
 */
void heap_sort(int *array, size_t size)
{
	int i;

	if (!size || !array)
		return;
	for (i = size / 2 - 1; i >= 0; i--)
	{
		maxHeapify(array, size, i, size);
	}
	for (i = size - 1; i > 0; i--)
	{
		if (array[0] >= array[i])
		{
			swap(&array[0], &array[i]);
			print_array(array, size);
		}
		maxHeapify(array, i, 0, size);
	}
}

/**
 * swap - swaps elements of arrays
 * @array1: pointer 1 element
 * @array2: pointer 2 element
 * Return: void
 */
void swap(int *array1, int *array2)
{
	int temp;

	temp = *array1;
	*array1 = *array2;
	*array2 = temp;
}
