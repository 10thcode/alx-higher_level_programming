#include "lists.h"

/**
 * print_dlistint - prints all the elements of a dlistint_t list.
 * @h: the head node of the list
 * Return: number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	if (h == NULL)
		return (0);
	
	printf("%d\n", h->n);

	return (print_dlistint(h->next) + 1);
}
