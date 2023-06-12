#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - a function in C that checks if a
 * singly linked list is a palindrome.
 *
 * @head: a pointer to the head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int len = get_list_lenght(*head);
	int i, j;

	for (i = 0, j = len - 1; i < len / 2; i++, j--)
		if (get_list_item(*head, i) != get_list_item(*head, j))
			return (0);

	return (1);
}

/**
 * get_list_lenght - get the number of node in a linked list
 * @head: the head node of the list
 * Return: the number of nodes in list
 */
int get_list_lenght(listint_t *head)
{
	if (head == NULL)
		return (0);

	if (head->next == NULL)
		return (1);

	return (get_list_lenght(head->next) + 1);
}

/**
 * get_list_item - get item from a linked list
 * @head: the head node of the list
 * @index: the position to retrieve item
 * Return: the item at index
 */
int get_list_item(listint_t *head, int index)
{
	int i;

	for (i = 0; head != NULL; head = head->next, i++)
		if (i == index)
			return (head->n);

	return (-1);
}
