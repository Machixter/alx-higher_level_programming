#include "lists.h"
/**
 * free_dlistint - frees all elements in a dlistint_t
 * @head: pointer to head of list
 * Return: nothing
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *current = head;
	dlistint_t *next;

	while (current)
	{
		next = current->next;
		free(current);
		current = next;
	}
}
