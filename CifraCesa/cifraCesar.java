import java.util.Scanner;

public class CifraDeCesar {
	public static void main(String[] args) {
	      Scanner ler = new Scanner(System.in);

	      System.out.printf("Informe um texto:\n");
	      String str = ler.nextLine().toUpperCase();	  
	      System.out.printf("Informe a chave:\n");
	      int y = ler.nextInt();
	      
	      String cript = criptografa(str);
	      System.out.printf("criptografado: %s \n",cript);
	      
	      System.out.printf("\n Informe a key para descriptografar ou 9999 para terminar o programa:\n");
	      int key = ler.nextInt();
	      
	      while(y != key) {
		      
		      System.out.printf("chave errada tente novamente:\n");
		      System.out.printf("Informe a key para descriptografar ou 9999 para terminar o programa:\n");
		      key = ler.nextInt();
		      if(key == 9999){
		          System.out.printf("Programa Finalizado \n");
		          break;
		      }
    	  }
    	  if(y == key){
    	        System.out.printf("descriptografado: %s \n", descriptografa(cript));
	            System.out.printf("Programa Finalizado\n");
    	  }
    	  
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

	    public static String descriptografa(String str) {
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
	    		  aux = aux + (char)(str.charAt(i) - 3);
	    	  }
	      }
	      return(aux);

	    }
}