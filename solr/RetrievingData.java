import java.io.IOException;  

import org.apache.Solr.client.Solrj.SolrClient; 
import org.apache.Solr.client.Solrj.SolrQuery; 
import org.apache.Solr.client.Solrj.SolrServerException; 
import org.apache.Solr.client.Solrj.impl.HttpSolrClient; 
import org.apache.Solr.client.Solrj.response.QueryResponse; 
import org.apache.Solr.common.SolrDocumentList;  

public class RetrievingData { 
   public static void main(String args[]) throws SolrServerException, IOException  { 
      //Preparing the Solr client 
      String urlString = "http://localhost:8983/Solr/my_core"; 
      SolrClient Solr = new HttpSolrClient.Builder(urlString).build();  
      
      //Preparing Solr query 
      SolrQuery query = new SolrQuery();  
      query.setQuery("*:*");  
   
      //Adding the field to be retrieved 
      query.addField("*");  
   
      //Executing the query 
      QueryResponse queryResponse = Solr.query(query);  
   
      //Storing the results of the query 
      SolrDocumentList docs = queryResponse.getResults();    
      System.out.println(docs); 
      System.out.println(docs.get(0)); 
      System.out.println(docs.get(1)); 
      System.out.println(docs.get(2));   
         
      //Saving the operations 
      Solr.commit();         
   } 
}
