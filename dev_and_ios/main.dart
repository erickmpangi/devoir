import 'package:flutter/material.dart';

void main() {
  runApp(SquareApp());
}

class SquareApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: SquareHome(),
    );
  }
}

class SquareHome extends StatefulWidget {
  @override
  _SquareHomeState createState() => _SquareHomeState();
}

class _SquareHomeState extends State<SquareHome> {
  final controller = TextEditingController();
  int? squareSize;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Tracer un carré")),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            TextField(
              controller: controller,
              decoration: InputDecoration(hintText: "Entrez un nombre"),
              keyboardType: TextInputType.number,
            ),
            ElevatedButton(
              onPressed: () {
                final value = int.tryParse(controller.text);
                if (value == null || value <= 0) {
                  ScaffoldMessenger.of(context).showSnackBar(
                    SnackBar(content: Text("Veuillez entrer un nombre positif"))
                  );
                } else {
                  setState(() {
                    squareSize = value;
                  });
                }
              },
              child: Text("Tracer le carré"),
            ),
            if (squareSize != null)
              Container(
                width: squareSize!.toDouble(),
                height: squareSize!.toDouble(),
                color: Colors.blue,
                margin: EdgeInsets.only(top: 20),
              ),
          ],
        ),
      ),
    );
  }
}
