#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *fast_pointer = list;
	listint_t *slow_pointer = list;

	while (fast_pointer != NULL && fast_pointer->next != NULL)
	{
		if (fast_pointer->next == slow_pointer)
			return (1);

		fast_pointer = fast_pointer->next->next;
		slow_pointer = slow_pointer->next;
	}

	return (0);
}
