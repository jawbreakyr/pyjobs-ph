<form method="post"
      action="">
      <legend>Company Details:</legend>
      <ul>
          <li>
              <label for="name">Name:</label>
              <br />
              <input type="text"
                     id="name"
                     name="name" />
          </li>
          <li>
              <label for="description">Description:</label>
              <p>
                  <textarea cols="30"
                            rows="5"
                            id="description"
                            name="description"></textarea>
              </p>
          </li>
          <li>
              <label for="uri">URI:</label>
              <br />
              <input type="text"
                     id="uri"
                     name="uri" />
          </li>
      </ul>
      <input type="submit"
             name="add"
             value="Add Company" />
</form>
