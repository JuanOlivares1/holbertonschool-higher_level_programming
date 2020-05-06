#include "lists.h"

/**
 * is_palindrome - says if a list is palindrome
 * @head: list's head
 *
 * Return: 1 if is palidrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int i, j, rtn = 1, len = 0, lasthalf;
	listint_t *head2, *back, *foward;

	head2 = *head;
	if (!head2)
		return (rtn);

	while (back != NULL)
	{
		len++;
		back = back->next;
	}
	lasthalf = len - (len / 2);
	for (i = 0; i < lasthalf; i++)
	{
		foward = head2;
		back = head2;
		for (j = 1; j <= (len - i - 1); j++)
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
