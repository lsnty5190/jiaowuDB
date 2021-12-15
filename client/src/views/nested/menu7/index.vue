<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>TEACHER</h1>
        <hr><br><br>
        <alert v-if="showMessage" :message="message" />
        <button v-b-modal.book-modal type="button" class="btn btn-success btn-sm">Add</button>
        &nbsp;
        <button v-b-modal.search-modal type="button" class="btn btn-success btn-sm">Search</button>
        &nbsp;
        <button type="button" class="btn btn-success btn-sm" @click="getBooks()">Flush</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Teacher_ID</th>
              <th scope="col">NAME</th>
              <th scope="col">gender</th>
              <th scope="col">Title</th>
              <th scope="col">Nation</th>
              <th scope="col">Email</th>
              <th scope="col">Dept_id</th>
              <th />
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ book.teacher_id }}</td>
              <td>{{ book.teacher_name }}</td>
              <td>{{ book.teacher_gender }}</td>
              <td>{{ book.teacher_title }}</td>
              <td>{{ book.teacher_nation }}</td>
              <td>{{ book.teacher_email }}</td>
              <td>{{ book.dept_id }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                    v-b-modal.book-update-modal
                    type="button"
                    class="btn btn-warning btn-sm"
                    @click="editBook(book)"
                  >
                    Update
                  </button>
                  <button
                    type="button"
                    class="btn btn-danger btn-sm"
                    @click="onDeleteBook(book)"
                  >
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal
      id="book-modal"
      ref="addBookModal"
      title="Add a new teacher"
      hide-footer
    >
      <b-form class="w-100" @submit="onSubmit" @reset="onReset">
        <b-form-group
          id="form-title-group"
          label="student_id:"
          label-for="form-title-input"
        >
          <b-form-input
            id="form-title-input"
            v-model="addBookForm.teacher_id"
            type="text"
            required
            placeholder="Enter Teacher_ID"
          />
        </b-form-group>
        <b-form-group
          id="form-author-group"
          label="Teacher_NAME:"
          label-for="form-author-input"
        >
          <b-form-input
            id="form-author-input"
            v-model="addBookForm.teacher_name"
            type="text"
            required
            placeholder="Enter Teacher_name"
          />
        </b-form-group>
        <b-form-group
          id="form-gender-group"
          label="Teacher_gender:"
          label-for="form-gender-input"
        >
          <b-form-input
            id="form-gender-input"
            v-model="addBookForm.teacher_gender"
            type="text"
            required
            placeholder="Enter Teacher_gender"
          />
        </b-form-group>
        <b-form-group
          id="form-tt-group"
          label="Teacher_title:"
          label-for="form-tt-input"
        >
          <b-form-input
            id="form-tt-input"
            v-model="addBookForm.teacher_title"
            type="text"
            required
            placeholder="Enter Teacher_title"
          />
        </b-form-group>
        <b-form-group
          id="form-nation-group"
          label="Teacher_nation:"
          label-for="form-nation-input"
        >
          <b-form-input
            id="form-nation-input"
            v-model="addBookForm.teacher_nation"
            type="text"
            required
            placeholder="Enter Teacher_nation"
          />
        </b-form-group>
        <b-form-group
          id="form-e-group"
          label="Teacher_email:"
          label-for="form-e-input"
        >
          <b-form-input
            id="form-e-input"
            v-model="addBookForm.teacher_email"
            type="text"
            required
            placeholder="Enter Teacher_email"
          />
        </b-form-group>
        <b-form-group
          id="form-dept-group"
          label="DEPT_ID:"
          label-for="form-dept-input"
        >
          <b-form-input
            id="form-dept-input"
            v-model="addBookForm.dept_id"
            type="text"
            required
            placeholder="Enter dept_id"
          />
        </b-form-group>
      
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal
      id="book-update-modal"
      ref="editBookModal"
      title="Update"
      hide-footer
    >
      <b-form class="w-100" @submit="onSubmitUpdate" @reset="onResetUpdate">
        <b-form-group
          id="form-title-group"
          label="student_id:"
          label-for="form-title-input"
        >
          <b-form-input
            id="form-title-input"
            v-model="editForm.teacher_id"
            type="text"
            required
            placeholder="Enter Teacher_ID"
          />
        </b-form-group>
        <b-form-group
          id="form-author-group"
          label="Teacher_NAME:"
          label-for="form-author-input"
        >
          <b-form-input
            id="form-author-input"
            v-model="editForm.teacher_name"
            type="text"
            required
            placeholder="Enter Teacher_name"
          />
        </b-form-group>
        <b-form-group
          id="form-gender-group"
          label="Teacher_gender:"
          label-for="form-gender-input"
        >
          <b-form-input
            id="form-gender-input"
            v-model="editForm.teacher_gender"
            type="text"
            required
            placeholder="Enter Teacher_gender"
          />
        </b-form-group>
        <b-form-group
          id="form-tt-group"
          label="Teacher_title:"
          label-for="form-tt-input"
        >
          <b-form-input
            id="form-tt-input"
            v-model="editForm.teacher_title"
            type="text"
            required
            placeholder="Enter Teacher_title"
          />
        </b-form-group>
        <b-form-group
          id="form-nation-group"
          label="Teacher_nation:"
          label-for="form-nation-input"
        >
          <b-form-input
            id="form-nation-input"
            v-model="editForm.teacher_nation"
            type="text"
            required
            placeholder="Enter Teacher_nation"
          />
        </b-form-group>
        <b-form-group
          id="form-e-group"
          label="Teacher_email:"
          label-for="form-e-input"
        >
          <b-form-input
            id="form-e-input"
            v-model="editForm.teacher_email"
            type="text"
            required
            placeholder="Enter Teacher_email"
          />
        </b-form-group>
        <b-form-group
          id="form-dept-group"
          label="DEPT_ID:"
          label-for="form-dept-input"
        >
          <b-form-input
            id="form-dept-input"
            v-model="editForm.dept_id"
            type="text"
            required
            placeholder="Enter dept_id"
          />
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>

    <b-modal
      id="search-modal"
      ref="searchBookModal"
      title="Search student"
      hide-footer
    >
      <b-form class="w-100" @submit="onSearch" @reset="onReset">
        <b-form-group
          id="form-title-group"
          label="student_id:"
          label-for="form-title-input"
        >
          <b-form-input
            id="form-title-input"
            v-model="searchForm.teacher_id"
            type="text"
            required
            placeholder="Enter Teacher_ID"
          />
        </b-form-group>
        <b-form-group
          id="form-author-group"
          label="Teacher_NAME:"
          label-for="form-author-input"
        >
          <b-form-input
            id="form-author-input"
            v-model="searchForm.teacher_name"
            type="text"
            required
            placeholder="Enter Teacher_name"
          />
        </b-form-group>
        <b-form-group
          id="form-gender-group"
          label="Teacher_gender:"
          label-for="form-gender-input"
        >
          <b-form-input
            id="form-gender-input"
            v-model="searchForm.teacher_gender"
            type="text"
            required
            placeholder="Enter Teacher_gender"
          />
        </b-form-group>
        <b-form-group
          id="form-tt-group"
          label="Teacher_title:"
          label-for="form-tt-input"
        >
          <b-form-input
            id="form-tt-input"
            v-model="searchForm.teacher_title"
            type="text"
            required
            placeholder="Enter Teacher_title"
          />
        </b-form-group>
        <b-form-group
          id="form-nation-group"
          label="Teacher_nation:"
          label-for="form-nation-input"
        >
          <b-form-input
            id="form-nation-input"
            v-model="searchForm.teacher_nation"
            type="text"
            required
            placeholder="Enter Teacher_nation"
          />
        </b-form-group>
        <b-form-group
          id="form-e-group"
          label="Teacher_email:"
          label-for="form-e-input"
        >
          <b-form-input
            id="form-e-input"
            v-model="searchForm.teacher_email"
            type="text"
            required
            placeholder="Enter Teacher_email"
          />
        </b-form-group>
        <b-form-group
          id="form-dept-group"
          label="DEPT_ID:"
          label-for="form-dept-input"
        >
          <b-form-input
            id="form-dept-input"
            v-model="searchForm.dept_id"
            type="text"
            required
            placeholder="Enter dept_id"
          />
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>

  </div>
</template>

<script>
import axios from 'axios'
import Alert from '@/components/Alert.vue'

export default {
  components: {
    alert: Alert
  },
  data() {
    return {
      books: [],
      addBookForm: {
        teacher_id: '',
        teacher_name: '',
        teacher_gender: '',
        teacher_title: '',
        teacher_nation: '',
        teacher_email: '',
        dept_id: ''
      },
      message: '',
      showMessage: false,
      editForm: {
        teacher_id: '',
        teacher_name: '',
        teacher_gender: '',
        teacher_title: '',
        teacher_nation: '',
        teacher_email: '',
        dept_id: ''
      },
      searchForm: {
        teacher_id: '',
        teacher_name: '',
        teacher_gender: '',
        teacher_title: '',
        teacher_nation: '',
        teacher_email: '',
        dept_id: ''
      }
    }
  },
  created() {
    this.getBooks()
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/teachers'
      axios.get(path)
        .then((res) => {
          this.books = res.data.books
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        })
    },
    addBook(payload) {
      const path = 'http://localhost:5000/teachers'
      axios.post(path, payload)
        .then(() => {
          this.getBooks()
          this.message = 'Teacher added!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks()
        })
    },
    searchBook(payload) {
        const path = 'http://localhost:5000/teachers/search'
        axios.post(path, payload)
            .then((res) => {
                this.books = res.data.books
            })
            .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
            })
    },
    initForm() {
      this.addBookForm.teacher_id = ''
      this.addBookForm.teacher_name = ''
      this.addBookForm.teacher_gender = ''
      this.addBookForm.teacher_title = ''
      this.addBookForm.teacher_nation = ''
      this.addBookForm.teacher_email = ''
      this.addBookForm.dept_id = ''

      this.editForm.teacher_id = ''
      this.editForm.teacher_name = ''
      this.editForm.teacher_gender = ''
      this.editForm.teacher_title = ''
      this.editForm.teacher_nation = ''
      this.editForm.teacher_email = ''
      this.editForm.dept_id = ''

      this.searchForm.teacher_id = ''
      this.searchForm.teacher_name = ''
      this.searchForm.teacher_gender = ''
      this.searchForm.teacher_title = ''
      this.searchForm.teacher_nation = ''
      this.searchForm.teacher_email = ''
      this.searchForm.dept_id = ''
    },
    onSubmit(evt) {
      evt.preventDefault()
      this.$refs.addBookModal.hide()
      // let read = false;
      // if (this.addBookForm.read[0]) read = true;
      const payload = {
        teacher_id: this.addBookForm.teacher_id,
        teacher_name: this.addBookForm.teacher_name,
        teacher_gender: this.addBookForm.teacher_gender,
        teacher_title: this.addBookForm.teacher_title,
        teacher_nation: this.addBookForm.teacher_nation,
        teacher_email: this.addBookForm.teacher_email,
        dept_id: this.addBookForm.dept_id,
      }
      this.addBook(payload)
      this.initForm()
    },
    onSearch(evt) {
      evt.preventDefault()
      this.$refs.searchBookModal.hide()
      // let read = false;
      // if (this.addBookForm.read[0]) read = true;
      const payload = {
        teacher_id: this.searchForm.teacher_id,
        teacher_name: this.searchForm.teacher_name,
        teacher_gender: this.searchForm.teacher_gender,
        teacher_title: this.searchForm.teacher_title,
        teacher_nation: this.searchForm.teacher_nation,
        teacher_email: this.searchForm.teacher_email,
        dept_id: this.searchForm.dept_id,
      }
      this.searchBook(payload)
      this.initForm()
    },
    onReset(evt) {
      evt.preventDefault()
      this.$refs.addBookModal.hide()
      this.initForm()
    },
    editBook(book) {
      this.editForm = book
    },
    onSubmitUpdate(evt) {
      evt.preventDefault()
      this.$refs.editBookModal.hide()
      // let read = false;
      // if (this.editForm.read[0]) read = true;
      const payload = {
        teacher_id: this.editForm.teacher_id,
        teacher_name: this.editForm.teacher_name,
        teacher_gender: this.editForm.teacher_gender,
        teacher_title: this.editForm.teacher_title,
        teacher_nation: this.editForm.teacher_nation,
        teacher_email: this.editForm.teacher_email,
        dept_id: this.editForm.dept_id,
      }
      this.updateBook(payload, this.editForm.teacher_id)
    },
    updateBook(payload, bookID) {
      const path = `http://localhost:5000/teachers/${bookID}`
      axios.put(path, payload)
        .then(() => {
          this.getBooks()
          this.message = 'teachers updated!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks()
        })
    },
    onResetUpdate(evt) {
      evt.preventDefault()
      this.$refs.editBookModal.hide()
      this.initForm()
      this.getBooks() // why?
    },
    removeBook(bookID) {
      const path = `http://localhost:5000/teachers/${bookID}`
      axios.delete(path)
        .then(() => {
          this.getBooks()
          this.message = 'teachers removed!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks()
        })
    },
    onDeleteBook(book) {
      this.removeBook(book.teacher_id)
    }
  }
}
</script>
