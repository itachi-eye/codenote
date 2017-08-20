package lambda;
/**
 * 使用lambda表达式
 * 
 */
public class ButtonAction {

	public static void main(String[] args) {

		Button btn = new Button();
		btn.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent event) {
				System.out.println("clicked: " + event);
			}
		});
		btn.click(); // simulate a butten clicked

		Button btn2 = new Button();
		btn2.addActionListener(event -> System.out.println("clicked2: " + event));
		btn2.click();

	}
}

// simulate a button
class Button {
	private ActionListener listener;

	public void addActionListener(ActionListener listener) {
		this.listener = listener;
	}

	public void click() {
		// create an event
		ActionEvent event = new ActionEvent("button-click-event", 100, 200);
		listener.actionPerformed(event);
	}
}

// simulate an event
class ActionEvent {
	private String msg;
	private int x;
	private int y;

	public ActionEvent(String msg, int x, int y) {
		this.msg = msg;
		this.x = x;
		this.y = y;
	}

	@Override
	public String toString() {
		return "ActionEvent [msg=" + msg + ", x=" + x + ", y=" + y + "]";
	}

}

// simulate an actionlistener
interface ActionListener {
	void actionPerformed(ActionEvent event);
}