#include "lists.h"
/**
 * print_dlistint - print number of list
 * @h: head node
 *
 * Return: number of nodees
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t n;

	n = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		n++;
	}

	return (n);

}
