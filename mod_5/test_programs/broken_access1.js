/* broken access 1 */

/* 
This example appears to fail to authenticate a user's user_id.
The attacker could just use any user_id and gain unauthorized access.
*/

app.get('/profile/:userId', (req, res) => {
    User.findById(req.params.userId, (err, user) => {
        if (err) return res.status(500).send(err);
        res.json(user);
    });
});

/*