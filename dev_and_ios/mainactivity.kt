package com.example.squareapp

import android.os.Bundle
import android.widget.EditText
import android.widget.Button
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val input = findViewById<EditText>(R.id.inputNumber)
        val button = findViewById<Button>(R.id.drawButton)

        button.setOnClickListener {
            val value = input.text.toString().toIntOrNull()
            if (value == null || value <= 0) {
                Toast.makeText(this, "Veuillez entrer un nombre positif", Toast.LENGTH_SHORT).show()
            } else {
                // Ici tu peux dessiner ton carré dans une View personnalisée
            }
        }
    }
}
