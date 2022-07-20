def test():
  # Read integers N and M from the standard input.
  (N, M) = tuple(map(int, input().split()))
  # Read N integers from the standard input and save them in the list `C`.
  C = list(map(int, input().split()))
  # Declare a variable for sum and set it to 0.
  sum = 0
  # Loop through the list `C` and sum its values.
  for Ci in C:
    sum += Ci
  # Compute the value of sum modulo M.
  modulo = sum % M
  # Print the result onto the standard output.
  print(modulo)


# Read the number of test cases.
T = int(input())
# Loop over the number of test cases.
for test_no in range(1, T + 1):
  # Print case number
  print("Case #%d:" % test_no, end=" ")
  # and solve each test.
  test() 



#####################################################################################################################################

  const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');
const btnCloseModal = document.querySelector('.btn--close-modal');
const btnsOpenModal = document.querySelectorAll('.btn--show-modal');

const openModal = function () {
  modal.classList.remove('hidden');
  overlay.classList.remove('hidden');
};

const closeModal = function () {
  modal.classList.add('hidden');
  overlay.classList.add('hidden');
};

for (let i = 0; i < btnsOpenModal.length; i++)
  btnsOpenModal[i].addEventListener('click', openModal);

btnCloseModal.addEventListener('click', closeModal);
overlay.addEventListener('click', closeModal);

document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
    closeModal();
  }
});

/////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////
const btnScrollTo = document.querySelector('.btn--scroll-to');
const section1 = document.querySelector('#section--1');

btnScrollTo.addEventListener('click', function (e) {
  const s1coords = section1.getBoundingClientRect();
  //Scrolling  effect
  section1.scrollIntoView({ behavior: 'smooth' });
});

const h1 = document.querySelector({ behavior: 'smooth' });

const alertH1 = function (e) {
  alert('addEventListener: Great! You are reading the heading :D');
};

h1.addEventListener('mouseenter', alertH1);

setTimeout(() => h1.removeEventListener('mouseenter', alertH1), 3000);

//Creation
const randomInt = (min, max) =>
  Math.floor(Math.random() * (max - min + 1) + min);
const randomColor = () =>
  `rgb(${randomInt(0, 255)},${randomInt(0, 255)},${randomInt(0, 255)})`;

document.querySelector('.nav__link').addEventListener('click', function (e) {
  this.style.backgroundColor = randomColor();
  console.log('LINK', e.target, e.currentTarget);
});
document.querySelector('.nav__links').addEventListener('click', function (e) {
  this.style.backgroundColor = randomColor();
  console.log('CONTAINER', e.target, e.currentTarget);
});

document.querySelector('.nav').addEventListener(
  'click',
  function (e) {
    this.style.backgroundColor = randomColor();
    console.log('NAV', e.target, e.currentTarget);
  },
  true
);

//Tabbed component
const tabs = document.querySelectorAll('.operation__tab');
const tabsContainer = document.querySelector('.operation__tab-container');
const tabsContent = document.querySelectorAll('.operation__content');

tabsContainer.addEventListener('click', function (e) {
  const clicked = e.target.parentElements;
  console.log(clicked);
});