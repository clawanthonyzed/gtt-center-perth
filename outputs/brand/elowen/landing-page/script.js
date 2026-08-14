/*
  GTT Center Perth (working placeholder name) — waitlist form behaviour.
  No backend is wired up yet. This file:
    1. Toggles the due-date field off when "not pregnant yet" is checked
       (a real UX necessity, not scope creep — a due-date input has no
       valid answer for that respondent otherwise; see
       docs/architecture/WAITLIST-VALIDATION-FRAMEWORK.md §1.1 for why
       this segment matters).
    2. Does basic client-side validation (native HTML5 required/type
       validation, plus a friendly inline message).
    3. On successful validation, shows the confirmation state.

  BEFORE THIS GOES LIVE: swap the placeholder handleSubmit body below for
  a real integration — e.g. a POST to Fresha/CRM, an email-service
  webhook (Resend, per docs/poppy-marketing.md §7), or a serverless form
  handler (Netlify Forms / Formspree-equivalent). Nothing here persists
  data anywhere yet — it is a working front-end scaffold, not a live
  data-collection endpoint.
*/

(function () {
  'use strict';

  var form = document.getElementById('waitlistForm');
  var confirmation = document.getElementById('formConfirmation');
  var notYetPregnantCheckbox = document.getElementById('notYetPregnant');
  var dueDateInput = document.getElementById('dueDate');

  if (notYetPregnantCheckbox && dueDateInput) {
    notYetPregnantCheckbox.addEventListener('change', function () {
      if (notYetPregnantCheckbox.checked) {
        dueDateInput.value = '';
        dueDateInput.disabled = true;
        dueDateInput.removeAttribute('required');
      } else {
        dueDateInput.disabled = false;
      }
    });
  }

  if (form) {
    form.addEventListener('submit', function (event) {
      event.preventDefault();

      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }

      var payload = {
        firstName: form.firstName.value.trim(),
        email: form.email.value.trim(),
        suburb: form.suburb.value.trim(),
        dueDate: notYetPregnantCheckbox.checked ? null : form.dueDate.value,
        notYetPregnant: notYetPregnantCheckbox.checked,
        referralSource: form.referralSource.value,
        submittedAt: new Date().toISOString()
      };

      // PLACEHOLDER — replace with a real submission call before launch.
      // e.g.: fetch('/api/waitlist', { method: 'POST', body: JSON.stringify(payload), headers: {'Content-Type':'application/json'} })
      console.log('Waitlist signup (placeholder, not sent anywhere yet):', payload);

      form.hidden = true;
      confirmation.hidden = false;
      confirmation.setAttribute('tabindex', '-1');
      confirmation.focus();
    });
  }
})();
