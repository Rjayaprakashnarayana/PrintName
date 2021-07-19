//Create an instance for the child class in child class and call non-abstract methods
public abstract class Test {

    void t1()
    {
        System.out.println("super");

    }

}
 public class concret extends Test{

    void t1()
{
    super.t1(); // First call the superclass implementation
    System.out.println("child");
}
    void t2()
    {
        System.out.println("child2");

    }

}

public class run {
    public static void main(String[] args) {
        Test t=new concret();

        t.t1();
    }

}