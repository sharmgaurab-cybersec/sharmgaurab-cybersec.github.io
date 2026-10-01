'use strict';

const copyButton = document.getElementById('copy-email');
const copyStatus = document.getElementById('copy-status');
let copyReset;
copyButton?.addEventListener('click', async () => {
  clearTimeout(copyReset);
  try {
    if (!navigator.clipboard?.writeText) throw new Error('Clipboard unavailable');
    await navigator.clipboard.writeText('sharmagaurab534@gmail.com');
    copyButton.textContent = 'Email copied';
    copyStatus.textContent = 'Email address copied to your clipboard.';
    copyReset = setTimeout(() => { copyButton.textContent = 'Copy email'; copyStatus.textContent = ''; }, 5000);
  } catch {
    copyStatus.textContent = 'Select the email address above to copy it, or use Email me.';
  }
});

function revealLinkedNote() {
  const note = document.getElementById(location.hash.slice(1));
  if (note?.matches('details')) note.open = true;
}
window.addEventListener('hashchange', revealLinkedNote);
revealLinkedNote();
