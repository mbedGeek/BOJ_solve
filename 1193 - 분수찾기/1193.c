//BOJ 1193 분수찾기

#include <stdio.h>

int main() {
    int i = 1, j = 2, k = 1, tmp = 0,  cnt = 1, n = 0, m = 0;

	scanf("%d", &i);

	while (i != 1) {
		tmp = k;
		k += j;
		++j;
		++cnt;

		if (i <= k) {
			break;
		}
	}

	if (i == 1) {
		printf("1/1");
		return 0;
	}

	i -= tmp;
	if ((cnt % 2) == 1) {
		m = cnt - (i - 1);
		n = j - m;
		printf("%d/%d", m, n);
	} else if ((cnt % 2) == 0) {
		n = cnt - (i - 1);
		m = j - n;
		printf("%d/%d", m, n);
	}

	return 0;
}