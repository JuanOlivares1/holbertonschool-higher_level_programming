#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - says if a list is palindrome
 * @head: list's head
 *
 * Return: 1 if is palidrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int i, j, rtn = 1;
	int list_len = 0, half, lasthalf;
	listint_t *head2, *current, *back, *foward;

	head2 = *head;
	if (!head2)
		return (rtn);
	current = head2;
	while (current->next != NULL)
	{
		list_len++;
		current = current->next;
	}
	list_len++;

	half = list_len / 2;
	lasthalf = list_len - half;
	for (i = 0; i < lasthalf; i++)
	{
		foward = head2;
		back = head2;
		for (j = 1; j <= (list_len - i - 1); j++)
		{
			back = back->next;
		}
		for (j = 1; j <= i; j++)
		{
			foward = foward->next;
		}
		if (foward->n != back->n)
		{
			rtn = 0;
			break;
		}
	}
	return (rtn);
}
