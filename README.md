# MealBridge
A platform that bridges the gap between restaurants with surplus food and NGOs striving to feed the underprivileged.


Our platform bridges the gap between restaurants with surplus food and NGOs striving to feed the underprivileged. It enables restaurants to register and post real-time food availability details, which are then instantly shared with verified NGOs in the same city via WhatsApp notifications. NGOs can view and claim these food drives through their dashboards, ensuring efficient redistribution. Each food request is closed upon acceptance to prevent duplication, and successful drives are dynamically recorded across the platform. The system includes an admin approval(checking Valid NGO Certifications/FSSAI Certificates) workflow, secure login for both parties, and onboarding emails for new users. By streamlining the donation process, we aim to reduce food wastage, promote social responsibility, and create a reliable ecosystem where every leftover meal finds a plate.


Basic System Design-
🔵 Landing Page (Public)

* Home: Overview and mission
* About Us: Include a dynamic count of successful drives (driven from the DB)
* Contact Us: Static
* Register as Restaurant / NGO: Clearly visible buttons
* Login Option: For both types of users


📝 Registration Flow

Fields:

Org Email, Name, City, Pincode, Google Map Link, Registration Certificate (file upload), Password

Flow:

1. Submits form → goes to Django Admin as a pending object
2. Admin approves (via admin panel)
3. Confirmation mail is sent on approval


🔄Set auto-set `is_active=False` on Django's User model and activate upon approval.


🔐Login System

* Single login with E-mail & Password


🍴 Restaurant Dashboard

* View connected drives (previously claimed requests)
* Create Request form:

  * Food Type (Veg / Non-Veg)
  * City is auto-filled from registration
* On submit:

  * Notify all NGOs in same city via WhatsApp
  * Message includes:

    * Food details
    * Google Maps link
    * Unique claim link



🙌 NGO Dashboard

* View connected drives (accepted and delivered)
* Logout

On clicking WhatsApp claim link:

* If logged in: go straight to Accept
* If not logged in: go to Login → redirect back to request



🔁 Request Acceptance

* One-click acceptance
* Close the request for others
* Mark it as Claimed by the NGO
* Increment the successful drives counter site-wide


