package cifraDeCesar;
import java.util.Scanner;

public class CifraDeCesar {
	public static void main(String[] args) {
	      Scanner ler = new Scanner(System.in);

	      System.out.printf("Informe um texto:\n");
	      String str = ler.nextLine().toUpperCase();	      

	      String cript = criptografa(str);
	      System.out.printf("criptografado: %s \n",cript);
	      
	      System.out.printf("Informe a key para descriptografar ou 9999 para terminar o programa:\n");
	      int key = ler.nextInt();
	      
	      while(key != 9999) {
		      System.out.printf("descriptografado: %s \n", descriptografa(cript,key));
		      System.out.printf("Informe a key para descriptografar ou 9999 para terminar o programa:\n");
		      key = ler.nextInt();
    	  }
	      System.out.printf("Programa Finalizado\n");
	      ler.close();
	      

	    }

	    public static String criptografa(String str) {
	      int i;
	      String aux = "";

		      for (i=0; i<str.length(); i++) {
		    	  if (str.charAt(i)=='X') {
		    		  aux= aux + 'A';
		    		  
		    	  }else if (str.charAt(i)=='Y') {
		    		  aux= aux + 'B';
		    		  
		    	  }else if (str.charAt(i)=='Z') {
		    		  aux= aux + 'C';
		    		  
		    	  }else{
		    		  aux = aux + (char)(str.charAt(i) + 3);
		    	  }
		      }
	      return(aux);
	      
	    }

	    public static String descriptografa(String str, int x) {
	      int i;
	      String aux = "";
	    	  
	      for (i=0; i<str.length(); i++) {

	    	  if (str.charAt(i)=='A') {
	    		  aux= aux + 'X';
	    		  
	    	  }else if (str.charAt(i)=='B') {
	    		  aux= aux + 'Y';
	    		  
	    	  }else if (str.charAt(i)=='C') {
	    		  aux= aux + 'Z';
	    		  
	    	  }	    	  else {
	    		  aux = aux + (char)(str.charAt(i) - x);
	    	  }
	      }
	      return(aux);

	    }
}
