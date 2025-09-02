import React, { useState } from 'react';
import { View, TextInput, Button, Text } from 'react-native';

export default function App() {
  const [value, setValue] = useState('');
  const [squareSize, setSquareSize] = useState(null);

  const handleDraw = () => {
    const num = parseInt(value);
    if (isNaN(num) || num <= 0) {
      alert("Veuillez entrer un nombre positif");
    } else {
      setSquareSize(num);
    }
  };

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <TextInput
        placeholder="Entrez un nombre"
        keyboardType="numeric"
        onChangeText={setValue}
        value={value}
        style={{ borderWidth: 1, padding: 10, width: 200, marginBottom: 10 }}
      />
      <Button title="Tracer le carré" onPress={handleDraw} />
      {squareSize && (
        <View style={{ width: squareSize, height: squareSize, backgroundColor: 'blue', marginTop: 20 }} />
      )}
    </View>
  );
}
