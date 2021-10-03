package program;

/**
 *
 * @author kizilkaya.c3411
 */
public class AisKineticChar {
    
    private String id;
    private String ais;
    private String kinetic;
    private String myChar;

    public AisKineticChar(String id, String ais, String kinetic, String myChar) {
        this.id = id;
        this.ais = ais;
        this.kinetic = kinetic;
        this.myChar = myChar;
    }
       
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
         
    public String getAis() {
        return ais;
    }

    public void setAis(String ais) {
        this.ais = ais;
    }

    public String getKinetic() {
        return kinetic;
    }

    public void setKinetic(String kinetic) {
        this.kinetic = kinetic;
    }

    public String getMyChar() {
        return myChar;
    }

    public void setMyChar(String myChar) {
        this.myChar = myChar;
    }

    @Override
    public String toString() {
        return "AisKineticChar{" + "id=" + id + ", ais=" + ais + ", kinetic=" + kinetic + ", myChar=" + myChar + '}';
    }      
        
}
