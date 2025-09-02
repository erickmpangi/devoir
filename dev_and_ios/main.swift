import UIKit

class SquareViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
    }

    func drawSquare(size: Int) {
        let square = UIView(frame: CGRect(x: 100, y: 200, width: size, height: size))
        square.backgroundColor = .blue
        view.addSubview(square)
    }
}
