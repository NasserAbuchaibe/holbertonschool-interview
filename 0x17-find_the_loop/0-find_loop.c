#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * *find_listint_loop - function that finds the loop in a linked list.
 * @head: pointer to a pointer to a list to the first element of a list.
 * Return: The address of the node where the loop starts, or NULL if there
 * is no loop
 */
listint_t *find_listint_loop(listint_t *head)
{
	listint_t *first, *second;

	first = head, second = head;
	if (head == NULL)
		return (NULL);
	while (second != NULL && first != NULL && second->next != NULL)
	{
		second = second->next->next;
		first = first->next;
		if (first == second)
		{
			first = head;
			while (first != second)
			{
				first = first->next;
				second = second->next;
			}
			return (second);
		}
	}
	return (NULL);
}
