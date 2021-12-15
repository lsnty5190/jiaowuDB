<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>STUDENT</h1>
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
              <th scope="col">Student_ID</th>
              <th scope="col">Student_NAME</th>
              <th scope="col">DEPT_ID</th>
              <th scope="col">TOT_CREDITS</th>
              <th />
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ book.student_id }}</td>
              <td>{{ book.student_name }}</td>
              <td>{{ book.dept_id }}</td>
              <td>{{ book.tot_credits }}</td>
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
      title="Add a new student"
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
            v-model="addBookForm.student_id"
            type="text"
            required
            placeholder="Enter Student_ID"
          />
        </b-form-group>
        <b-form-group
          id="form-author-group"
          label="Student_NAME:"
          label-for="form-author-input"
        >
          <b-form-input
            id="form-author-input"
            v-model="addBookForm.student_name"
            type="text"
            required
            placeholder="Enter Student_name"
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
        <b-form-group
          id="form-cedit-group"
          label="Course_Credit:"
          label-for="form-credit-input"
        >
          <b-form-input
            id="form-credit-input"
            v-model="addBookForm.tot_credits"
            type="text"
            required
            placeholder="Enter Total_Credits"
          />
        </b-form-group>
        <!-- <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addBookForm.read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group> -->
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
            v-model="editForm.student_id"
            type="text"
            required
            placeholder="Enter student_id"
          />
        </b-form-group>
        <b-form-group
          id="form-author-group"
          label="student_name:"
          label-for="form-author-input"
        >
          <b-form-input
            id="form-author-input"
            v-model="editForm.student_name"
            type="text"
            required
            placeholder="Enter student_name"
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
        <b-form-group
          id="form-cedit-group"
          label="TOT_Credits:"
          label-for="form-credit-input"
        >
          <b-form-input
            id="form-credit-input"
            v-model="editForm.tot_credits"
            type="text"
            required
            placeholder="Enter TOT_Credits"
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
            v-model="searchForm.student_id"
            type="text"
            
            placeholder="Enter Student_ID"
          />
        </b-form-group>
        <b-form-group
          id="form-author-group"
          label="Student_NAME:"
          label-for="form-author-input"
        >
          <b-form-input
            id="form-author-input"
            v-model="searchForm.student_name"
            type="text"
            
            placeholder="Enter Student_name"
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
            
            placeholder="Enter dept_id"
          />
        </b-form-group>
        <b-form-group
          id="form-cedit-group"
          label="Course_Credit:"
          label-for="form-credit-input"
        >
          <b-form-input
            id="form-credit-input"
            v-model="searchForm.tot_credits"
            type="text"
            
            placeholder="Enter Total_Credits"
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
        student_id: '',
        student_name: '',
        dept_id: '',
        tot_credits: ''
      },
      message: '',
      showMessage: false,
      editForm: {
        student_id: '',
        student_name: '',
        dept_id: '',
        tot_credits: ''
      },
      searchForm: {
        student_id: '',
        student_name: '',
        dept_id: '',
        tot_credits: ''
      }
    }
  },
  created() {
    this.getBooks()
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/students'
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
      const path = 'http://localhost:5000/students'
      axios.post(path, payload)
        .then(() => {
          this.getBooks()
          this.message = 'Student added!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks()
        })
    },
    searchBook(payload) {
        const path = 'http://localhost:5000/students/search'
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
      this.addBookForm.student_id = ''
      this.addBookForm.student_name = ''
      this.addBookForm.dept_id = ''
      this.addBookForm.tot_credits = ''

      this.editForm.student_id = ''
      this.editForm.student_name = ''
      this.editForm.dept_id = ''
      this.editForm.tot_credits = ''

      this.searchForm.student_id = ''
      this.searchForm.student_name = ''
      this.searchForm.dept_id = ''
      this.searchForm.tot_credits = ''
    },
    onSubmit(evt) {
      evt.preventDefault()
      this.$refs.addBookModal.hide()
      // let read = false;
      // if (this.addBookForm.read[0]) read = true;
      const payload = {
        student_id: this.addBookForm.student_id,
        student_name: this.addBookForm.student_name,
        dept_id: this.addBookForm.dept_id,
        tot_credits: this.addBookForm.tot_credits
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
        student_id: this.searchForm.student_id,
        student_name: this.searchForm.student_name,
        dept_id: this.searchForm.dept_id,
        tot_credits: this.searchForm.tot_credits
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
        student_id: this.editForm.student_id,
        student_name: this.editForm.student_name,
        dept_id: this.editForm.dept_id,
        tot_credits: this.editForm.tot_credits
      }
      this.updateBook(payload, this.editForm.student_id)
    },
    updateBook(payload, bookID) {
      const path = `http://localhost:5000/students/${bookID}`
      axios.put(path, payload)
        .then(() => {
          this.getBooks()
          this.message = 'Student updated!'
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
      const path = `http://localhost:5000/students/${bookID}`
      axios.delete(path)
        .then(() => {
          this.getBooks()
          this.message = 'Student removed!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks()
        })
    },
    onDeleteBook(book) {
      this.removeBook(book.student_id)
    }
  }
}
</script>
