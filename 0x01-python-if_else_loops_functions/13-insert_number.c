#include "lists.h"

/**
 * insert_node - insert a number into at desired place in a list
 * @head: pointer to the head of the list
 * @number: number to be inserted
 *
 * Return: success pointer to the new node fail null
 **/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;
	new->next = node->next;
	node->next = new;
	return (new);
}
