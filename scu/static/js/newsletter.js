// document.getElementById("newsletter-signup-form").addEventListener("submit", (e) => {
//   e.preventDefault();
//   const email = e.target.elements[0].value;
//   if (email && email.includes("@")) {
//       fetch(e.target.action, {
//           method: e.target.method,
//           body: JSON.stringify({email: email})
//       })
//       .then(response => response.json())
//       .then(data => {
//           if (data.success) {
//               alert("All signed up! Thank you for joining the newsletter!")
//           }
//       })
//       .catch(err => {
//           alert("Looks like we're having an error. Please try again in a moment.")
//       });
//   }    
// });