#include "lists.h"
/**
 * dlistint_len - return number of lements in a linked dlistint_t list
 * @h: head of linked list
 * Return: number of nodes as size_t
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t count = 0;
	const dlistint_t *current = h;
	while (current != NULL)
	{
		count++;
		current = current->next;
	}
	return (count);
}
