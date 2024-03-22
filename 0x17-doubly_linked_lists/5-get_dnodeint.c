#include "lists.h"
/**
 * get_dnodeint_at_index - returns nth node od dlistint_t
 * @head: pointer to head of list
 * @index: index of node
 * Return: nth node of list
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *current = head;
	unsigned int count = 0;

	while (current != NULL)
	{
		if (count == index)
		{
			return (current);
		}
		current = current->next;
		count++;
	}
	return (NULL);
}
