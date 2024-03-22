#include "lists.h"
/**
 * insert_dlistint_at_index - inserts new node at given position
 * @idx: idex position of new_node
 * @n: pointer to new_node
 * @head: pointer to start of list
 * Return: n
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n){
	dlistint_t *new_node = malloc(sizeof(dlistint_t));
	dlistint_t *current = *h;
	unsigned int i = 0;

	if (new_node == NULL)
		return (NULL);

	new_node->n = n;

	if (idx == 0){
		new_node->next = *h;
		new_node->prev = NULL;
		if (*h != NULL)
			(*h)->prev = new_node;
		*h = new_node;
	} else {
		while (current != NULL && i < idx -1){
			current = current->next;
			i++;

		}
		if (current == NULL){
			free(new_node);
			return (NULL);
		}
		new_node->next = current->next;
		new_node->prev = current;
		if (current->next != NULL)
			current->next->prev = new_node;
		current->next = new_node;

	}
	return (new_node);
}

