#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: a pointer to the head of the list
 * @number: the number to be inserted
 * Return: new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *temp;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (*head == NULL)	/* empty list */
	{
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}
	if ((*head)->n > number)	/* beginning of list */
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	temp = *head;
	while (temp->next != NULL)	/* middle and end of list */
	{
		if (temp->next->n > number)
			break;
		temp = temp->next;
	}
	new_node->next = temp->next;
	temp->next = new_node;
	return (new_node);
}
