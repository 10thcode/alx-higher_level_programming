#include "lists.h"

/**
 * is_palindrome - a function that checks if
 * a singly linked list is a palindrome.
 * @head: a pointer to the head node of the list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *previous = NULL, *current = *head, *tail = *head, *l1, *l2;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (tail != NULL && tail->next != NULL)
	{
		tail = tail->next->next;
		*head = (*head)->next;
		current->next = previous;
		previous = current;
		current = *head;
	}

	l1 = previous;
	if (tail == NULL)
		l2 = current;
	else
		l2 = current->next;

	for (; l1 != NULL; l1 = l1->next, l2 = l2->next)
		if (l1->n != l2->n)
			return (0);

	return (1);
}
