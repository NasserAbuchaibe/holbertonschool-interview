#include "search_algos.h"

/**
 * print_array - Print array or subarray
 * @array: array to be printed
 * @begin: beginning of array
 * @end: end of  array
 */
void print_array(int *array, int begin, int end)
{
	int x;

	printf("Searching in array: ");
	for (x = begin; x <= end; x++)
	{
		if (x != begin)
			printf(", ");
		printf("%d", array[x]);
	}
	printf("\n");
}

/**
 * recursive_binary_search - Finds value in array recursivelly
 * @array: array to be searched its value
 * @begin: beginning of array (left)
 * @end: end of array (rigth)
 * @value: value to be searched
 * Return: index of value or -1
 */
int recursive_binary_search(int *array, int begin, int end, int value)
{
	if (end >= begin)
	{
		int middle = begin + (end - begin) / 2;

		print_array(array, begin, end);
		if (array[middle] == value)
		{
			if (array[middle - 1] == value)
				return (recursive_binary_search(array, begin, middle, value));

			return (middle);
		}
		if (array[middle] >= value)
			return (recursive_binary_search(array, begin, middle, value));
		return (recursive_binary_search(array, middle + 1, end, value));
	}
	return (-1);
}

/**
 * advanced_binary - Calls recursive binary search function
 * @array: array to be searched its value
 * @size: size of array
 * @value: value to be searched
 * Return: index of value otherwise -1
 */
int advanced_binary(int *array, size_t size, int value)
{
	if (!array)
		return (-1);
	return (recursive_binary_search(array, 0, size - 1, value));
}
