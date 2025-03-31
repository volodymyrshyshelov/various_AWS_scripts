let input = document.getElementById('result');

function appendNumber(number) {
  input.value += number;
}

function appendOperator(operator) {
  input.value += operator;
}

function calculate() {
  try {
    input.value = eval(input.value);
  } catch (error) {
    input.value = 'Ошибка';
  }
}

function deleteLastCharacter() {
  input.value = input.value.slice(0, -1);
}

function makeNegative() {
  if (input.value.charAt(0) === '-') {
    input.value = input.value.slice(1);
  } else {
    input.value = '-' + input.value;
  }
}

function calculateSqrt() {
  try {
    input.value = Math.sqrt(eval(input.value));
  } catch (error) {
    input.value = 'Ошибка';
  }
}

function calculatePercent() {
  try {
    input.value = eval(input.value) / 100;
  } catch (error) {
    input.value = 'Ошибка';
  }
}

function calculateInverse() {
  try {
    input.value = 1 / eval(input.value);
  } catch (error) {
    input.value = 'Ошибка';
  }
}
    function clearExpression() {
  input.value = '';
}
