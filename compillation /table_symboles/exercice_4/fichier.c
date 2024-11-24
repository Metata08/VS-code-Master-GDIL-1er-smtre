/* la fonction somme(int,int) renvoie la somme de ses arguments */ 

int somme(int a, int b){
	return a + b;
}

int main(void)
{
	printf("somme(5,9) = %d\n", somme(5,9));
	getchar();
	// getchar() attend un retour chariot
	return 0;
}