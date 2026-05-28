/** Coefficients from trained LinearRegression (see ml/medical_insurance_model.pkl). */
const MODEL = {
  intercept: 11357.668742540951,
  coef: {
    age: 251.4051219591732,
    sex: 26.117159659121654,
    bmi: 330.64637156848545,
    children: 580.2743829604781,
    smoker: -23928.1017106112,
    region: 212.22242728332387,
  },
};

const SEX_MAP = { male: 0, female: 1 };
const SMOKER_MAP = { yes: 0, no: 1 };
const REGION_MAP = {
  southeast: 0,
  southwest: 1,
  northeast: 2,
  northwest: 3,
};

function predict({ age, sex, bmi, children, smoker, region }) {
  const features = {
    age: Number(age),
    sex: SEX_MAP[sex],
    bmi: Number(bmi),
    children: Number(children),
    smoker: SMOKER_MAP[smoker],
    region: REGION_MAP[region],
  };

  let total = MODEL.intercept;
  for (const [name, value] of Object.entries(features)) {
    total += MODEL.coef[name] * value;
  }
  return total;
}

function formatCurrency(amount) {
  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    maximumFractionDigits: 2,
  }).format(amount);
}

const form = document.getElementById("predict-form");
const resultEl = document.getElementById("result");
const resultValueEl = document.getElementById("result-value");

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const data = Object.fromEntries(new FormData(form));
  const charge = predict(data);

  resultValueEl.textContent = formatCurrency(charge);
  resultEl.hidden = false;
});
