#include "lists.h"
/**
 * add_dnodeint - adds a node to the head of linked list
 * @head: pointer to head of struct
 * @n: pointer to str that adds as a node
 * Return: NULL or new head of list
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *rem;
	

	rem = malloc(sizeof(dlistint_t));
	if (rem == NULL)
		return (NULL);


	rem->n = n;
	rem->prev = NULL;
	rem->next = *head;
	if (*head != NULL)
		(*head)->prev = rem;
	*head = rem;
	return (rem);
}

